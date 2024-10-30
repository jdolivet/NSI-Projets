"use client";

import { CanvasHTMLAttributes, DetailedHTMLProps, useEffect, useLayoutEffect, useRef } from "react";
import shader from '@/files/shader';

import "@/styles/components/GLGradient.scss";
import styles from "@/styles/components/GLGradient.module.scss";

declare global {
  let shaderWebBackground: any;
}

export default function GLGradient(props: DetailedHTMLProps<CanvasHTMLAttributes<HTMLCanvasElement>, HTMLCanvasElement>) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const shaderRef = useRef<HTMLScriptElement>(null);

  function shade() {
    // @ts-ignore
    shaderWebBackground.shade({
      canvas: canvasRef.current,
      shaders: {
        Image: {
          uniforms: {
            iTime: (gl: any, loc: any) => gl.uniform1f(loc, performance.now() / 1000),
            iResolution: (gl: any, loc: any, ctx: any) => gl.uniform2f(loc, ctx.width, ctx.height),
            iScrolled: (gl: any, loc: any) => gl.uniform1f(loc, window.scrollY / window.innerHeight),
            iLightMode: (gl: any, loc: any) => gl.uniform1i(loc, window.matchMedia("(prefers-color-scheme: light)").matches ? 1 : 0),
            iDarkMode: (gl: any, loc: any) => gl.uniform1i(loc, window.matchMedia("(prefers-color-scheme: dark)").matches ? 1 : 0)
          }
        }
      }
    });
  }

  useLayoutEffect(shade, [canvasRef]);

  return (
    <>
      <script src="/shader-web-background.min.js" />
      <script
        ref={shaderRef}
        type="x-shader/x-fragment"
        id="Image"
        dangerouslySetInnerHTML={{ __html: shader }}
      />
      <canvas {...props} className={`${styles.canvas} ${styles.fallback}`} ref={canvasRef} />
    </>
  )
}
