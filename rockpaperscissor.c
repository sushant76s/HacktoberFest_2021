#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROCK 1
#define PAPER 2
#define SCISSORS 3
#define P1WIN 4
#define P2WIN 5
#define DRAW 6

int whoWon(int, int);
int getUserInput();

int whoWon(int p1, int p2)
{
    int output;
    if (p1 == ROCK && p2 == PAPER)
    {
        output = P2WIN;
    }
    else if (p1 == PAPER && p2 == SCISSORS)
    {
        output = P2WIN;
    }
    else if (p1 == SCISSORS && p2 == ROCK)
    {
        output = P2WIN;
    }
    else if (p1 == PAPER && p2 == ROCK)
    {
        output = P1WIN;
    }
    else if (p1 == SCISSORS && p2 == PAPER)
    {
        output = P1WIN;
    }
    else if (p1 == ROCK && p2 == SCISSORS)
    {
        output = P1WIN;
    }
    else
    {
        output = DRAW;
    }
    return output;
}

int getUserInput()
{
    int inp;
    do
    {
        printf("1 = rock\n");
        printf("2 = paper\n");
        printf("3 = scissors\n");

        printf("Enter the users' choice: ");
        scanf("%d", &inp);
        if (!(inp >= 1 && inp <= 3))
        {
            printf("Error --impropper inputs\n");
            printf("Enter the users' choice: ");
            scanf("%d", &inp);
        }

    } while (!(inp >= 1 && inp <= 3));
    return inp;
}

int main()
{
    int x;
    int y;
    int i;
    int z;
    int userscore = 0;
    int Machinescore = 0;
    char exit;
    srand(time(NULL));
    for (i = 0;; i++)
    {
        x = getUserInput();
        y = (rand() % 3 + 1);
        z = whoWon(x, y);

        if (z == P1WIN)
        {
            printf("user won this round\n");
            userscore++;
        }
        else if (z == P2WIN)
        {
            printf("computer won this round\n");
            Machinescore++;
        }
        else
        {
            printf("draw\n");
        }

        if (y == 1)
        {
            printf("computer chose rock\n");
        }
        else if (y == 2)
        {
            printf("computer chose paper\n");
        }
        else
        {
            printf("computer chose scissors\n");
        }

        printf("do you want to exit(y/Y) or any key to continue: ");
        scanf(" %c", &exit);
        if (exit == 'y' || exit == 'Y')
        {
            break;
        }
        else
        {
            continue;
        }
    }
    printf("----------------------------------\n");
    printf("\t user score = %d\n", userscore);
    printf("----------------------------------\n");
    printf("----------------------------------\n");
    printf("\t computer score = %d\n", Machinescore);
    printf("----------------------------------\n");

    return 0;
}
