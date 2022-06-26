// Veginere's Cipher + Ceaser Cipher
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define LSIZE 1000
//# define RSIZE 100
unsigned char matrix[256][256];
unsigned char key[10] = "hello";
char cfile[LSIZE];

int shift=2;


//void string_input(){
    
    //scanf("%[^\n]%*c",cfile);
    //scanf("\n");
    //scanf("%[^\n]%*c",key);
    //scanf("%d",&shift);

//}
void cipher(int shift){
    for (int i =0; cfile[i]!=0;i++)
    {
        cfile[i]+=shift;

    }

}

void de_cipher(int shift){
    for (int i =0; cfile[i]!=0;i++)
    {
        cfile[i]-=shift;
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



// make a keyword equal to the length of the cfile accepted
void makeKeyword(char* key){
    unsigned char p[strlen(cfile)];
    
    
    int i=0,j=0;
    
    
    for(i=0,j=0;i<strlen(cfile);i++,j++){
        if(j==strlen(key))
            j=0;
        p[i]=key[j];
    }
        
    p[strlen(cfile)]='\0';  
    strcpy(key,p);//makes as hellohellohell and assigned it as key
}

// encrypts a letter,  key taken as row head and cfile as column head
unsigned char encryptLetter(char t,char k){
    int kp,tp; //key position and cfile position

    // for key position for row
    for(int i=0, j=0;j<256;j++){  // row kept constant
        if (k==matrix[i][j]){     //in first row the position of H is found
            kp=j;  
            break;

        }
    }

    
    for(int i=0, j=0;i<256;i++){
        if (t==matrix[i][j]){     //in the first column the position of C is found out
            tp=i;
            break;

        }
    }

    //return matrix[kp][tp]; //point where the C and H coincides
    return matrix[tp][kp];
}

void encrypt(){
    unsigned char p;
    
    for(int i=0;i<strlen(cfile);i++){
        p= encryptLetter(cfile[i],key[i]);
        cfile[i]=p;
    }
    cfile[strlen(key)]='\0';
}

//decrypts a letter
unsigned char decryptLetter(char t,char k){
    int kp,tp;

    
    kp=k;
    
    // for encryted cfile position for column
    for(int i=0, j=k;i<256;i++){
        
        if (t==matrix[i][k]){ // fixing the col
            tp=i;
            break;

        }
    }
    
    return matrix[tp][0];
}


//for decrypting the cfile
void decrypt(){
    for(int i = 0; i < strlen(cfile); ++i)
        cfile[i] = (((cfile[i] - key[i]) + 256) % 256) ;
 
    cfile[strlen(cfile)] = '\0';
    printf("The cfile returned after encryption and decryption is: %s\n",cfile);
    
}



int main()
{
   FILE *fptr;
   int i=0;
   //int n=0;
   fptr=fopen("data.txt","r");
   if(fptr==NULL){
       printf("Cannot open the file");
   }
   while(!(feof(fptr))){
    cfile[i]=fgetc(fptr);
    //fscanf(fptr,"%s",&cfile[i]);
    i++;
    
   }
  
    
    makeMatrix();
    //string_input();
    
    makeKeyword(key);
    //printf("%d\n",strlen(cfile));
    //printf("%d\n",strlen(key));

    printf("The multiplied keyword : %s\n",key);

    printf("The cfile to be encrypted: %s\n",cfile);
    

        

    
    
    encrypt();
    printf("The encrypted cfile: %s\n",cfile);

    cipher(shift);
    printf("The encrypted ciphered cfile: %s\n",cfile);


    
    de_cipher(shift);
    printf("Deciphered which returns the encrypted back: %s\n",cfile);
    
    //strcpy(cfile,"Computer Science 67");
    decrypt();


    
    fclose(fptr);
  
    return 0;
}