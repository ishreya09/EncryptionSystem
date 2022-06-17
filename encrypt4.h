unsigned char text[10000];
void key_init(unsigned char *k);
void text_init(unsigned char *t);
void shift_init(int s);
unsigned char get_text();
void string_input();
void cipher(int shift);
void de_cipher(int shift);
void makeMatrix();
void printMatrix();
void makeKeyword(char* key);
unsigned char encryptLetter(unsigned char t,unsigned char k);
void encrypt();
void decrypt();


