// Veginere's Cipher + Ceaser Cipher
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <errno.h>

// GUI 
// FILE HANDLING

char matrix[256][256];
char key[10000];
char text[10000];
char address[2000];
int shift;

//getters for python
char* getText(){
    return text;
}

char* getKey(){
    return key;
}

char* getAddress(){
    return address;
}

int getShift(){
    return shift;
}


// setters
void key_init(char *k){
    strcpy(key,k);
}

void text_init(char *t){
    strcpy(text,t);
}


void shift_init(int s){
    shift=s;
}

void address_init(char *add){
    strcpy(address,add);
}

void file_input(){

    printf("Enter the file to be encrypted :- ");
    scanf("\n%[^\n]%*c",address);
    printf("Enter the key :- ");
    scanf("\n%[^\n]%*c",key);
    printf("Enter the shift value for caeser cipher :- ");
    scanf("%d",&shift);

}

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
    char k=-128;

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
void makeKeyword(){
    char p[strlen(text)];
    // char *p;
    // p = (char*)calloc(strlen(text),sizeof(char));
    

    int i=0,j=0;
    
    for(i=0,j=0;i<strlen(text);i++,j++){
        if(j==strlen(key))
            j=0;
        p[i]=key[j];
    }
        
    p[strlen(text)]='\0';

    printf("%s\n",key);  

    strcpy(key,p);//makes the key of same length as text length
}


char encryptLetter(char t,char k){
    int kp,tp;

    // for key position for row and text position for col
    kp=k;
    tp=t;

    return matrix[kp][tp];
}

void encrypt(){
    char p;
    
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
    FILE *fp;
    fp= fopen(address,"r");
    if (fp==NULL){
        printf("Could not open files");
        exit(0);

    }
    // else {

    //     char t[10000],ch;
    //     int i=0;
    //     while ((ch=fgetc(fp))!=EOF){
    //         t[i++]=ch;
    //     }
    else{
        char t[10000];
        int i=0;
        while(!(feof(fp))){
            t[i]=fgetc(fp);
            i++;
        }
        t[i]='\0';
        
        text_init(t); // key and shift will be assigned by python gui
        fclose(fp);
    }
    
}

void write_another_file(char *add){
    FILE *fp;
    fp = fopen(add,"w");
    if (fp==NULL){
        printf("Could not open files");
        exit(0);
    }

    else
    {
        char ch;
        int i=0;
        // global text
        while (text[i]!=0){
            printf("%c",text[i]);
            fputc(text[i],fp);
            i++;
        }
        fclose(fp);
    }

}

void write_file(){
    FILE *fp;
    fp = fopen(address,"w");
    if (fp==NULL){
        printf("Could not open files");
        exit(0);
    }

    else
    {
        char ch;
        int i=0;
        // global text
        while (text[i]!=0){
            printf("%c",text[i]);
            fputc(text[i],fp);
            i++;
        }
        fclose(fp);
    }

}

// to create a shared library
// cc -fPIC -shared -o encrypt.so encrypt.c


int main(){
    int choice; 

    do{
        printf("Hello\n");
        printf("WELCOME TO THE ENCRYPTION AND DECRYPTION SYSTEM");
        printf("What do you wish to encrypt....?\n");
        printf("A string or a file....\n");
        printf("Choice 1: Wishing to encrypt strings \n");
        printf("Choice 2:Wishing to encrypt the file\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);


    
        switch(choice){
            case 1:
            string_input();
            printf("Do you wish to encrypt or decrypt...??\n");
            printf("Choice 1: Encrypt the string\n");
            printf("Choice 2: Decrypt the string\n");
            int option;
            scanf("%d",&option);
            switch(option){
                case 1:
                encrypt();
                printf("%d\n",text==0);
                printf("%s\n",text);
                break;
                case 2 :
                decrypt();
                printf("%s\n",text);
                break;
                default:
                break;
            }
            break;
            case 2:
            file_input();
            printf("Do you wish to encrypt or decrypt...??\n");
            printf("Choice 1: Encrypt the file\n");
            printf("Choice 2: Decrypt the file\n");
            int opt;
            scanf("%d",&opt);
            switch(opt){
                case 1:
                input_file();
                encrypt();
                write_file();
                printf("%s\n",text);
                break;
                case 2 :
                input_file(); 
                decrypt();
                write_file();
                printf("%s\n",text);
                break;
                default:
                break;
            }
            break;
            default:
                printf("Invalid Choice");


        }
    }while (choice>0 && choice<3);

}