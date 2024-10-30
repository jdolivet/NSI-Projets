import styles from '@/styles/components/Cat.module.scss';
import ComputerAscii from './ComputerAscii';

export default function Cat() {
  return (
    <>
      <ComputerAscii />
      <div className={styles.catbox}>
        <div />
        <div>
          <div />
          <CatAscii />
          <div />
        </div>
      </div>
    </>
  );
}

function CatAscii() {
  // I am so sorry.
  return <pre id="cat" dangerouslySetInnerHTML={{
    __html: `              z
          z
      z
    ,
   \\)\\_
  /    '. .---._
=P -     \`      '.
 \`--.       /     \\
    .-'(    \\      |
(.-'   )-..__>   , ;
(_.--\`\`    (__.-/ /
        .-.__.-'.'
         '-...-'`}}></pre>
}

