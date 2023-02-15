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

    s = s + (s / 3) - (s / 4);

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
