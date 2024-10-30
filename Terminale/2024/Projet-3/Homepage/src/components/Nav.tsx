import CopyAnchor from "./CopyAnchor";
import styles from "@/styles/components/Nav.module.scss"
import tooltip from "@/styles/util/tooltip.module.scss"
import Link from "next/link";


export default function Nav() {
  return (
    <nav className={styles.nav}>
      <Link className={styles.header} href="/">
        <h1>zoe's website</h1>
      </Link>
      <div />
      <ul>
        <li>
          <Link
            href="https://github.com/zoeleu"
            target="_blank"
            referrerPolicy="no-referrer"
          >
            github
          </Link>
        </li>
        <li>
          <CopyAnchor role="button" href="#" copy="8x13b">
            discord
          </CopyAnchor>
        </li>
        <li>
          <Link href="/blog">blog</Link>
        </li>
        <li>
          <Link href="/wallpaper">
            wallpaper
          </Link>
        </li>
      </ul>
    </nav>
  )
}