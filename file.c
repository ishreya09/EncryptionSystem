// deals with file handling of the functions
#include<stdio.h>
#include <stdlib.h>
#include "encrypt4.c"
// need an header file + a .so file so that it can be called in the gui of python

int input_file(char address[2000]){
    FILE *fp;
    fp= fopen(address,"r");
    if (fp==NULL){
        //do something to prompt the error
        // maybe error handing of C in files
        return -1;
    }
    else {
        unsigned char t[10000],ch;
        int i=0;
        while (ch=fgetc(fp)){
            t[i++]=ch;
        }
        t[i]='\0';
        
        text_init(t); // key and shift will be assigned by python gui
        fclose(fp);
        return 1;
    }
}

void write_file(char address[2000]){
    FILE *fp;
    fp = fopen(address,"w");
    unsigned char t[10000],ch;
    strcpy(t,get_text());
    int i=0;
    while (t[i]!=0){
        fputc(t[i],fp);
        i++;
    }
    t[i]='\0';
    fclose(fp);

}



// no need for main
// check in a different dir on how r+ works
