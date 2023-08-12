int p = 1;
int seq [16];

void Fin()
{
  while (true)
  {
    digitalWrite(2, HIGH);
    delay(200);
    digitalWrite(2, LOW);
    delay(200);
  }
}

void Anim(int d) // animation pour quand un bonton est appuyé
{
  digitalWrite(d, HIGH);
  delay(200);
  digitalWrite(d, LOW);
}



void setup()
{
  randomSeed(analogRead(0));
  for (int i = 0; i < 16; ++i)
  {
    seq[i] = (random(4)) + 2;
  }
  //setup des boutons      bouton   LED
  pinMode(6, INPUT_PULLUP);  //6 == 3  bleu
  pinMode(7, INPUT_PULLUP);  //7 == 2  rouge
  pinMode(8, INPUT_PULLUP);  //8 == 5  vert
  pinMode(9, INPUT_PULLUP);  //9 == 4  jaune


  //setup des LED
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);


  //petite animation stylé au debut
  for (int i = 1; i <= 3; ++i)
  {
    digitalWrite(2, HIGH);
    delay(100);
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    delay(100);
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    delay(100);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
    delay(100);
    digitalWrite(5, LOW);
  }
  delay(3000);
}
void loop()
{
  //montre le shema des led + ajout un random
  for (int i = 0; i < p ; ++i)
  {
    delay(450);
    digitalWrite((seq[i]), HIGH);
    delay(450);
    digitalWrite((seq[i]), LOW);
    delay(450);
  }

  //bouton == LED

  for (int i = 0; i < p ; ++i)
  {
    while (true)
    {
      // LED verte   8 == 5
      if (digitalRead(8) ==  LOW)
      {
        Anim(5);
        if (seq[i] == 5)
        {
          break;
        }
        else
        {
          Fin();
        }
      }
      // LED rouge  7 == 2
      if (digitalRead(7) ==  LOW)
      {
        Anim(2);
        if (seq[i] == 2)
        {
          break;
        }
        else
        {
          Fin();
        }
      }
      // LED jaune  9 == 4
      if (digitalRead(9) ==  LOW)
      {
        Anim(4);
        if (seq[i] == 4)
        {
          break;
        }
        else
        {
          Fin();
        }
      }
      // LED bleu  6 == 3
      if (digitalRead(6) ==  LOW)
      {
        Anim(3);
        if (seq[i] == 3)
        {
          break;
        }
        else
        {
          Fin();
        }
      }
    }
  }
  ++p;// ajoute 1 à p
}
