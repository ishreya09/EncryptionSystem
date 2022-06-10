// Veginere's Cipher + Ceaser Cipher
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

// GUI 
// FILE HANDLING

unsigned char matrix[256][256];
unsigned char key[10000];
unsigned char text[10000];
int shift;
void string_input(){

    printf("Enter the text to be encrypted :- ");
    scanf("\n%[^\n]%*c",text);
    printf("Enter the key :- ");
    scanf("\n%[^\n]%*c",key);
    printf("Enter the shift value for caeser cipher :- ");
    scanf("%d",&shift);

}


void cipher(int shift){
    for (int i =0; text[i]!=0;i++)
    {
        text[i]+=shift;

    }

}

void de_cipher(int shift){
    for (int i =0; text[i]!=0;i++)
    {
        text[i]-=shift;
    }
}


// to make a 256*256 matrix for veginere's cipher
void makeMatrix(){
    unsigned char k=0;

    for(int i=0;i<256;i++){
        k=i;
        for (int j=0;j<256;j++){
            matrix[i][j]= k++;
        }
    }

}


// to print the matrix for veginere's cipher
void printMatrix(){

    for(int i=0;i<256;i++){
        
        for (int j=0;j<256;j++){
            printf("%d\t",matrix[i][j]);
        }
        printf("\n");
    }

}



// make a keyword equal to the length of the text accepted
void makeKeyword(char* key){
    unsigned char p[strlen(text)];
    
    
    int i=0,j=0;
    
    
    for(i=0,j=0;i<strlen(text);i++,j++){
        if(j==strlen(key))
            j=0;
        p[i]=key[j];
    }
        
    p[strlen(text)]='\0';  
    strcpy(key,p);//makes as hellohellohell and assigned it as key
}


unsigned char encryptLetter(unsigned char t,unsigned char k){
    int kp,tp;

    // for key position for row and text position for col
    kp=k;
    tp=t;

    return matrix[kp][tp];
}

void encrypt(){
    unsigned char p;
    
    for(int i=0;i<strlen(text);i++){
        p= encryptLetter(text[i],key[i]);
        text[i]=p;
    }
    text[strlen(key)]='\0';
}



// for decrypting the text
void decrypt(){
       for(int i = 0; i < strlen(text); ++i)
        text[i] = (((text[i] - key[i]) + 256) % 256) ;
 
    text[strlen(text)] = '\0';
}

void input_file(){
    
}



int main()
{
    int shift;
    makeMatrix();
    
    printf("Enter the text to be encrypted :- ");
    scanf("\n%[^\n]%*c",text);
    printf("Enter the key :- ");
    scanf("\n%[^\n]%*c",key);
    printf("Enter the shift value for caeser cipher :- ");
    scanf("%d",&shift);
    makeKeyword(key);

    printf("\nThe multiplied keyword : \n%s\n",key);

    printf("\nThe text to be encrypted:\n%s\n",text);

    encrypt();
    printf("\nThe encrypted text: \n%s\n",text);

    cipher(shift);
    printf("\nThe encrypted ceaser ciphered text: \n%s\n",text);

    de_cipher(shift);
    printf("\nDe ceaser ciphered which returns the encrypted back: \n%s\n",text);
    decrypt();
    printf("\nThe text returned after decryption is: \n%s\n\n",text);

    return 0;
}

