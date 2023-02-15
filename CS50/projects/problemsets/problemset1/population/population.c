#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int s;      //Start Size
    do
    {
        s = get_int("Start size: ");
    }
    while (s < 9);

    int e;      //End size
    do
    {
        e = get_int("End size: ");
    }
    while (e < s);

    int years = 0;

    while (s < e)
    {
        s = s + (s / 3) - (s / 4);
        years++;
    }
    printf("Years: %i\n", years);
}
