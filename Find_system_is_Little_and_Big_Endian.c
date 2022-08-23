
void lit_big(char *val, int n){
    int i;
    for(i=0; i<n; i++){
        printf("%.2x",val[i]);
    }
    printf("\n");
}

int main() {
	int a = 0x01234567;
	lit_big((char *)&a, sizeof(a));
    printf("\n");
    
    // Second solution
    unsigned int i=1;
    char *b= (char *)&i;
    if (*b){
        printf("Little endian");
    }
    else{
        printf("Big endian");
    }
	return 0;
}
