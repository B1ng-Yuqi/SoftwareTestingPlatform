code = r'''0 void ModuleX (int x, int y, int Wid, char *Str) 
  {
1    unsigned Zcode, Bcode; 
2    int i, j, k, Rec, Color; 
3    long Len; 
4    char Buf[72]; 
5    while (*Str) 
     {
6        if ((*Str & 0x80) && (*(Str+1) & 0x80))
         {
7             Zcode = (*Str - 0xa1) & 0x07f;
8             Bcode = (*(Str + 1) - 0xa1) & 0x07f;
9             Rec = Zcode*94 + Bcode;
10            Len = Rec*72L;
11            fseek(fp, Len, SEEK_SET);
12            fread (Buf, 1, 72, fp);
13            for (i = 0; i < 24; i++) 
14                for (j = 0; j < 3; j++) 
15                    for (k = 0; k < 8; k++) 
16                        if (Buf[i*3 + j] >> (7 - k) & 1) 
                          { 
17                            Color = y + j*8 + k - 46; 
18                            PutPoint(x + i, y + j*8 + k, Color); 
18-1                      }
19            x = x + 24 + Wid;
20            Str += 2;
6-1        }
5-1    } 
21    return;
  }'''
