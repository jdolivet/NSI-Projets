'use client';

import { AnchorHTMLAttributes, DetailedHTMLProps, useEffect, useState } from "react";
import styles from "@/styles/util/tooltip.module.scss"

export default function CopyAnchor(props: DetailedHTMLProps<AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement> & { copy: string }) {
  const [tooltip, setTooltip] = useState(props.copy);
  const [css, setCss] = useState<string>(
    `#tooltip-${styles.tooltip}:hover::after { content: "${tooltip}" }`
  );

  const delay = (ms: number) => new Promise(
    resolve => setTimeout(resolve, ms)
  );

  function click() {
    navigator.clipboard.writeText(props.copy);

    setTooltip("copied!");
  }

  useEffect(() => {
    async function handle() {
      setCss(`#tooltip-${styles.tooltip}:hover::after { content: "${tooltip}" }`);
      await delay(3000);
      setTooltip(props.copy);
      setCss(`#tooltip-${styles.tooltip}:hover::after { content: "${tooltip}" }`);
    }
    handle()
  }, [tooltip]);

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: css }} />
      <a {...props} className={styles.tooltip} id={`tooltip-${styles.tooltip}`} data-tooltip={props.copy} onClick={click}>
        {props.children}
      </a>
    </>
  )
}