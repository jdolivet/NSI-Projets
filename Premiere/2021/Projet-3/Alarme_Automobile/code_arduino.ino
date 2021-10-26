// inclusion des bibliothèques et fonction utilisés
#include <LiquidCrystal.h> 
#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd; 

// definition de la couleur du background du Backlight RGB
const int colorR = 0;
const int colorG = 0;
const int colorB = 255;

// definition des pins d'entrées
#define IN4  4           // pour le buzzer
const int trigPin = 5;   // pour le pin du Trig du capteur
const int echoPin = 6;   // pour le pin de l'echo du capteur
const int buttonPin = 7; // pour le bouton

// definition des variables
long duration;
int distance = 0;
int red = 9;

void setup() { // Definit des regles avant le fonctionnement
  pinMode(trigPin, OUTPUT); // Definit le trigPin comme sortie
  pinMode(echoPin, INPUT); // Definit le trigPin comme entrée
  pinMode(4, OUTPUT);
  pinMode(red, OUTPUT);
  int buttonPin = 6;
  Serial.begin(9600); // Débute la communication 
  lcd.begin(16, 2); //Defini nombre de ligne et col dpour le backlight
  lcd.print("Distance: "); // Message qui apparait sur le backlight
}

void loop() { // Debut de la boucle infinit
  if (digitalRead(buttonPin) == HIGH) { // Active code si bouton est allumée
      lcd.display();
      lcd.setRGB(colorR, colorG, colorB);
      if ((distance < 5) && (distance > 0)) // Les distances sont en cm
      { // Allume le buzzer et le LED constamment
        digitalWrite(IN4, HIGH);
        digitalWrite(red, HIGH);
      }
      else if ((distance > 5) && (distance < 30)) //si distance est comprise entre 5cm et 30cm, 
      //la vitesse des intervalles est progressivement décroissante quand plus on s'approche
      { 
        digitalWrite(IN4, HIGH); // Allume le buzzer
        delay(10 * (distance - 5)); // Formule buzzer et LED s'allume dependant de la distance
        digitalWrite(IN4, LOW); // Eteint le buzzer
        delay(10 * (distance - 5));
        digitalWrite(red, HIGH); // Allume le LED
        delay(10 * (distance - 5));
        digitalWrite(red, LOW); // Eteint le LED
        delay(10 * (distance - 5));
        delayMicroseconds(2);
      }
      else if (distance > 30) { // Si distance > 30 cm, de buzzer et LED sont éteints
        digitalWrite(IN4, LOW);
        digitalWrite(red, LOW);
      }
      {
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10); // Active le trigPin pour 10 microsecondes 
      digitalWrite(trigPin, LOW);
      duration = pulseIn(echoPin, HIGH); // Lis le echopin et renvoie la distance en cm
      distance = duration * 0.034 / 2; // Formule pour calc la distance 
      Serial.print("Distance: "); // Print ce string dans le terminal
      Serial.println(distance); // Print la distance dans le terminal
      Serial.println("cm"); // Print ce string dans le terminal
      lcd.setCursor(0, 1); // Positionnement du text dans le backlight
      lcd.print(duration * 0.034 / 2); // Formule pour montrer la distance dans blacklight mise a jour a temps réel
      lcd.setCursor(14, 1);
      lcd.print("cm"); //Affiche l'unité des distance dans le backlight
      delay(100);
      }  
    }
  if (digitalRead(buttonPin) == LOW) { // Eteindre le programme si bouton n'est pas appuyee
        digitalWrite(IN4, LOW);   
        digitalWrite(red, LOW);
        lcd.setRGB(colorR, colorG, 0);
        lcd.noDisplay();
      }
  }
