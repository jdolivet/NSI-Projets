import Image from "next/image";
import styles from "@/styles/pages/Index.module.scss";
import CatAscii from "@/components/Cat";
import GLGradient from "@/components/GLGradient";

export default function Home() {
  return (
    <div className={styles.page}>
      <CatAscii />
    </div>
  );
}
