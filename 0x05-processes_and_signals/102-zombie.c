#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - loop
 * Return: 0
 */

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - zombie
 * Return: 0
 */

int main(void)
{
    int idx = 0;
    pid_t pid;

    while (idx <= 5)
    {
        pid = fork();
        if (pid > 0)
        {
            sleep (1);
        }
        else
        {
            exit(0);
        }
        printf("Zombie process created, PID: %d\n", pid);
        idx++;
    }
    infinite_while();
    return (0);
}