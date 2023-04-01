#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  char flag[64];
  char *flag_ptr = flag;

  puts("Spune-i lui ochila unde sa se uite, si o sa iti spuna ce vede");

  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("flag.txt nu e aici!\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);

  while(1) {
    printf("Unde ?\n");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }
  return 0;
}
