"use client";

import puterFrames from "@/files/puter";
import { PropsWithChildren, useEffect, useLayoutEffect, useState } from "react";
import styles from "@/styles/components/Cat.module.scss";

interface ComputerAsciiProps { }

export default function ComputerAscii(props: PropsWithChildren<ComputerAsciiProps>) {
  const [currentFrame, setCurrentFrame] = useState(0);

  function run() {
    if (currentFrame >= (puterFrames.length - 1)) {
      setCurrentFrame(puterFrames.length - 2);
    } else {
      setCurrentFrame(currentFrame + 1);
    }
  }

  useEffect(() => {
    const intervalId = setInterval(run, 500);

    return () => clearInterval(intervalId);
  }, [currentFrame]);

  return (
    <pre className={styles.puter} id="computer">
      {puterFrames[currentFrame % puterFrames.length]}
    </pre>
  );
}