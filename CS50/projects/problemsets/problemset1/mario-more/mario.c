#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 0 || h > 8);

    for (int r = 0; r < h; r++)
    {
        for (int c = 0; c <= r; c++)
        {
            printf("#");
        }
    printf("\n");
    }
}