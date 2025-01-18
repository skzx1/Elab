ตารางหมากรุก
หมากรุกสากลเป็นเกมส์กระดานแนววางแผนสองผู้เล่น ที่เล่นบนกระดานสลับสีซึ่งมีจัตุรัส 64 ช่อง จัดเรียงแบบ 8x8 ช่อง
ประกอบด้วยตัวหมาก 6 ประเภท คือ King (ราชา), Queen (ราชินี), Knight (อัศวิน), Bishop (นักบวช), Rook (เรือ) และ Pawn (เบี้ย)

ให้เขียนโปรแกรมเพื่อแสดงตำแหน่งของตัวหมากบนตารางหมากรุกสากลในเกมหนึ่ง
โดย บรรทัดที่ 1 รับจำนวนเต็ม numPieces ที่แสดงจำนวนตัวหมากที่เหลืออยู่บนกระดาน
บรรทัดที่ 2 ถึง บรรทัดที่ numPieces + 1 รับตัวอักษร pieceChar ที่แทนตัวหมากและพิกัด x, y บนกระดาน ในรูปแบบ pieceChar(x, y) (พิกัดมุมซ้ายบนของตารางคือ 0, 0 และ พิกัดมุมขวาล่างของตารางคือ 7, 7)

ตัวอักษร pieceChar ที่แทนตัวหมากมีความหมายดังนี้

K แทน King
Q แทน Queen
N แทน Knight
B แทน Bishop
R แทน Rook
P แทน Pawn
ตัวอักษรตัวใหญ่ แทน ตัวหมากของผู้เล่น 1 และ ตัวอักษรตัวเล็ก แทน ตัวหมากของผู้เล่น 2

บรรทัดที่ numPieces + 2 เป็นต้นไป แสดงตำแหน่งของตัวหมากบนตาราง

ตัวอย่างโปรแกรม

4
k(4, 0)
K(4, 7)
b(3, 4)
B(4, 5)
------------------
  0 1 2 3 4 5 6 7
0| | | | |k| | | |
1| | | | | | | | |
2| | | | | | | | |
3| | | | | | | | |
4| | | |b| | | | |
5| | | | |B| | | |
6| | | | | | | | |
7| | | | |K| | | |



#include <stdio.h>
#include <stdlib.h>
#define BOARD_SIZE 8

void setPieceOnTable(int board[][BOARD_SIZE], char piece, int xPos, int yPos);

int main()
{
    int board[BOARD_SIZE][BOARD_SIZE] = {0};
    int n, numj = 0, numi = 0;
    scanf("%d", &n);
    char pieces[n];
    int moves[n][2];

    for (int i = 0; i < n; i++)
    {
        scanf(" %c(%d, %d)", &pieces[i], &moves[i][0], &moves[i][1]);
        setPieceOnTable(board, pieces[i], moves[i][0], moves[i][1]);
    }
    printf("------------------\n");
    for (int i = 0; i < BOARD_SIZE + 1; i++)
    {
        if (i != 0)
        {
            printf("%d", numi);
            numi++;
        }
        for (int j = 0; j < 17; j++)
        {
            if (i == 0 && j != 0 && j != 1 && j % 2 == 0)
            {
                printf("%d", numj);
                numj++;
            }
            else if (j % 2 == 0 && i != 0)
            {
                printf("|");
            }
            else if (i > 0 && j % 2 == 1 && (j / 2) < BOARD_SIZE && board[i - 1][j / 2] != 0)
            {
                printf("%c", board[i - 1][j / 2]);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}

void setPieceOnTable(int board[][BOARD_SIZE], char piece, int xPos, int yPos)
{
    board[yPos][xPos] = piece;
}