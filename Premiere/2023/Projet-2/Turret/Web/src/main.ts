import './style.css'
import {
  PoseLandmarker,
  FilesetResolver,
  DrawingUtils,

} from '@mediapipe/tasks-vision'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = /* html */`
    <button id="connectbutton">Connecter</button>
    <div style="position: relative;">
      <video id="webcam" style="width: 1280px; height: 720px; position: abso" autoplay playsinline></video>
      <canvas class="output_canvas" id="output_canvas" width="1280" height="720" style="position: absolute; left: 0px; top: 0px; z-index:9999;"></canvas>
    </div>
`

let poseLandmarker: PoseLandmarker | undefined = undefined;
let runningMode = "IMAGE";
let webcamRunning: Boolean = true;
const videoHeight = "360px";
const videoWidth = "480px";
let buttonPromiseResolve = () => {};
let buttonPromise = new Promise<void>((resolve, _) => {
  buttonPromiseResolve = resolve;
});
document.querySelector("button#connectbutton")?.addEventListener("click", buttonPromiseResolve);

// Chargement asynchrone du système de detection
const createPoseLandmarker = async () => {
  const vision = await FilesetResolver.forVisionTasks(
    // CDN pour le fichier de code Web Assembly relationé à Tensorflow
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
  );
  poseLandmarker = await PoseLandmarker.createFromOptions(vision, {
    baseOptions: {
      // Modèle pour l'IA
      modelAssetPath: `https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task`,
      // Execution sur carte graphique pour performance plus haute
      delegate: "GPU"
    },
    // Mode VIDEO et non IMAGE
    runningMode: "VIDEO",
    // Seulement une cible supportée
    numPoses: 1
  });
};
createPoseLandmarker().then(() => navigator.serial.getPorts())
  .then(async (ports) => {
    // Arduino Uno
    let usbVendorId = 0x2341;
    let usbProductId = 0x0043;

    // On attend une action de l'utilisateur
    await buttonPromise;

    return navigator.serial.requestPort({ filters: [{ usbProductId, usbVendorId }] })
  })
  .then(async (port) => {
    await port.open({ baudRate: 115200 });

    if (port.writable) {
      return port.writable;
    } else {
      throw new Error("Serial port not writable");
    }
  })
  .then(async (port) => {
    // Video de la caméra
    const video = document.getElementById("webcam") as HTMLVideoElement;
    const canvasElement = document.getElementById(
      "output_canvas"
    ) as HTMLCanvasElement;
    // Points de corps
    const canvasCtx = canvasElement.getContext("2d")!;
    // Classe utilitaire pour les dessiner
    const drawingUtils = new DrawingUtils(canvasCtx);

    // Vérification du support à camera
    const hasGetUserMedia = () => !!navigator.mediaDevices?.getUserMedia;

    // Si l'utilisateur n'a pas les fonctions nécessaires, on le previent
    if (!hasGetUserMedia()) {
      alert("Manque de getUserMedia()");
    }

    const devices = await navigator.mediaDevices.enumerateDevices();

    const device = devices.find((v) => v.label.includes("OBS"));

    // Activer la caméra.
    navigator.mediaDevices.getUserMedia({
      video: {
        facingMode: "environment", // Prendre la caméra arrière dans les smartphones
        deviceId: device!.deviceId
      }
    }).then((stream) => {
      video.srcObject = stream;
      // À chaque image, appeller la fonction d'estimation
      video.addEventListener("loadeddata", predictWebcam);
    });


    let lastVideoTime = -1;
    let writer = port.getWriter();
    let encoder = new TextEncoder();
    async function predictWebcam() {
      canvasElement.style.height = videoHeight;
      video.style.height = videoHeight;
      canvasElement.style.width = videoWidth;
      video.style.width = videoWidth;
      // Now let's start detecting the stream.
      if (runningMode === "IMAGE") {
        runningMode = "VIDEO";
        await poseLandmarker!.setOptions({ runningMode: "VIDEO" });
      }
      let startTimeMs = performance.now();
      if (lastVideoTime !== video.currentTime) {
        lastVideoTime = video.currentTime;
        poseLandmarker!.detectForVideo(video, startTimeMs, (result) => {
          canvasCtx.save();
          canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
          for (const landmark of result.landmarks) {
            drawingUtils.drawLandmarks(landmark, {
              radius: (data) => DrawingUtils.lerp(data.from!.z, -0.15, 0.1, 5, 1)
            });
            drawingUtils.drawConnectors(landmark, PoseLandmarker.POSE_CONNECTIONS);
            let angleX = 85 - (((landmark[0].x - 0.5) * 85) + 85/2);
            // Pour utilisation prochaine
            // let angleY = (landmark[0].y - 0.5) * 47.8125;
            console.log(angleX)
            writer.write(encoder.encode(Math.round(angleX).toString() + "\n"));
          }
          canvasCtx.restore();
        });
      }

      // Call this function again to keep predicting when the browser is ready.
      if (webcamRunning === true) {
        window.requestAnimationFrame(predictWebcam);
      }
    }
  });