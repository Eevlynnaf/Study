#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int startsize;
    do
    {
        startsize = get_int("Positive Integer: ");
    }
    while (startsize <= 9);

    int endsize;
    do
    {
        endsize = get_int("Positive Integer: ");
    }
    while (endsize >= startsize);

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
