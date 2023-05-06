// C++ code


//  The circuit:
//  * LCD RS pin to digital pin 11
// * LCD Enable pin to digital pin 10
// * LCD D4 pin to digital pin 5
// * LCD D5 pin to digital pin 4
// * LCD D6 pin to digital pin 3
// * LCD D7 pin to digital pin 2
// * LCD R/W pin to ground
// * LCD VSS pin to ground
// * LCD VCC pin to 5V
// * 10K resistor:
// * ends to +5V and ground
// * wiper to LCD VO pin (pin 3)



//function : delay() >> delay(1000) = attends 1 seconde
//function : millis() >> temps depuis le debut du code, en ms



#include <LiquidCrystal.h> //importe le module permettant d'utiliser l'écran lcd

int time = 0;
int t1 = 0;
int t2 = 0;
int ft = 0;

LiquidCrystal lcd(11, 10, 5, 4, 3, 2); //on informe quelles ports de la arduino sera utilisé pour l'écran LCD

void setup()
{
	lcd.begin(16, 2); // L'écran du LCD a un format 16x2.

	// Print un message sur le LCD
 	lcd.print("Reaction Time");
 	//le bouton, pin 13
 	pinMode(13, INPUT_PULLUP);
 	//la DEL, pin 12
 	pinMode(12, OUTPUT);
 

}

void loop()
{
 	int ctd = rand() % 7 + 2; //prend un nombre au hasard entre 2 (inclu) et 7 (exclu)
 	ctd *= 1000; //multiplie la valeur obtenue par 1000 pour obtenir des milisecondes
	int sensorVal = digitalRead(13); // lit la position du button connecté au port 13
  	digitalWrite(12, LOW); // eteint la DEL au pin 12
  	delay(ctd); // attend le nombre de milisecondes choisit au hasard
  	t1 = millis(); // mesure le temps depuis le debut l'execution du programme, à cette instant (en ms)
  	digitalWrite(12, HIGH); // allume la DEL au pin 12
  	//boucle infini qui verifie si le button est appuyé
  	while(true) {
    	int sensorVal = digitalRead(13); // verifie la position du button dans chaque boucle
    	if (sensorVal == LOW) {
      		t2 = millis();  // mesure d'un deuxieme temps
      		digitalWrite(12, LOW); //éteint la led au pin 12
      		break; //sort de la boucle infini
   		}
 	}
 	// écrit sur la 2eme ligne
 	lcd.setCursor(0, 1);
 	ft = (t2 - t1); // la difference entre les deux mesures prises (le temps entre l'éclairage de la led et le pressage du button)
 	lcd.print(ft / 1000.0); // convertie des milisecondes en secondes
 	delay(2000); // attends 2 secondes

 	while(true) {  //attends que le button soit réappuyé pour réexecuter le programme (boucle)
    	int sensorVal = digitalRead(13);
      if (sensorVal == LOW) {
      	lcd.clear();
      	lcd.print("Reaction Time");
      	break;
    	}
  	}
}