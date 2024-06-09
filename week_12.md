# Arrays and lists

* Definition of *static* arrays: size defined at compile time

* Initialization

* Indexing

* `while` and `for` loops

* The function `sizeof`

* Arrays as input of a function

* Functions prototypes

* The `include` statement

```c
#include <stdio.h>

int sum(int[], int);

int main(){
    int a[5]; /* an array of 5 undefined integers */
    float b[3] = {0.1, 3.14, 2.71}; /* an array of 3 defined floats */
    int c[15] = {3, 1}; /*first item is 3, second is 1, the orther are 0*/

    int i = 0;
    while ( i < 5 ){
        printf("a[%d] = %d\n", i, a[i] );
        i += 1; /*but also i++;*/
    }

    i = 0;
    while ( i < 3 ){
        printf("b[%d] = %.2f\n", i, b[i] );
        i += 1; /*but also i++;*/
    }

    c[13] = 21;

    for(i=0; i < 15; i++){
        printf("c[%d] = %d\n", i, c[i] );
    }

    /*
     * The same of
     * 
     * i = 0
     * while (i < 15){
     *         printf("c[%d] = %d\n", i, c[i] );
     *         i++;
     * }
     * 
     * */

     printf("the size of a is %d bytes\n", sizeof(a));

     int n = sizeof(b)/sizeof(int);  /*the size (number of items) of b*/

     printf("%d\n", n);

     n = sizeof(c)/sizeof(int);

     printf("The sum of integers in c is %d\n", sum(c, n) );


    for(i=0; i < 15; i++){
        printf("c[%d] = %d\n", i, c[i] );
    }
}

int sum(int v[], int n){
    int i, s = 0;

    for(i=0; i < n; i++){
        s += v[i];
        v[i] = 0; /* modifies the original array*/
    }

    return s;
}
```

* Arrays defined at runtime

* Array and pointers

* The `malloc` function of the `stdlib` library

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int *p; /*a pointer to an integer*/
    int i;

    p = malloc(4*sizeof(int));

    for(i=0; i < 4; i++){
        p[i]= i*10;
    }

    for(i=0; i < 4; i++){
        printf("%d\n", p[i]);
    }
}
```

Writing a function that returns an array.

```c
#include<stdio.h>
#include<stdlib.h>

int *new_array_wrong(int);
int *new_array(int);

int main(){
    int *p = new_array(5);
    int i;

    for(i = 0; i < 5; i++){
        printf("%d\n", p[i]);
    }
}


int *new_array_wrong(int n){
    int a[n]; /*a local variable*/

    for(int i=0; i < n; i++){
        a[i] = 0;
    }

    return a; /*the address of the first byte of a*/

    /*
     * we are returning an address of a local array. When
     * the function ends, that array will be de-allocated
     * 
     * */
}

int *new_array(int n){
    int *a = malloc(n*sizeof(int));

    for(int i=0; i < n; i++){
        a[i] = 0;
    }

    return a; /*the address of the first byte of a*/

    /*
     * we are returning an address of a space that remanins
     * allocated after the end of the function
     *  
     * */
}
```

* The `struct` and `typedef` statemets
* Towards the designing of a dynamic array (list): a first expensive solution
* Description of the efficient solution

```c
#include<stdio.h>
#include<stdlib.h>

struct list {
    int *p; /*array of integers */
    int n; /* number of items in the list*/
};
typedef struct list list;


list zeros(int);
void show(list);
list append(list, int);

int main(){
    list a, b, c; /*the same of struct list */
    int i;

    a.p = malloc(4*sizeof(int));
    a.n = 4;

    a.p[2] = 12;
    printf("%d\n", a.p[2] + 1);

    printf("===========================\n");

    b = zeros(12);
    show(b);

    printf("===========================\n");

    c = zeros(1);
    for(i = 1; i < 5; i++){
        c = append(c, i);
        show(c);
    }
}

list zeros(int n){
    list x;

    x.n = n;

    if (n <= 0 ) 
        x.p = NULL;
    else
        x.p = malloc(n*sizeof(int));

    for(int i = 0; i < x.n; i++){
        x.p[i] = 0;
    }

    return x;
} 

void show(list x){
    int i;

    printf("[");
    for(i=0; i < x.n; i++){
        printf("%d ", x.p[i]); 
    }
    printf("]\n");
}

list append(list x, int e){
    int *q = malloc((x.n+1)*sizeof(int));
    int i;

    for( i = 0; i < x.n; i++){
        q[i] = x.p[i];
    }
    q[x.n] = e;

    free(x.p);
    x.p = q;
    x.n += 1;

    return x;
}
```

* Implementation of the `append` function that guarantees constant time complexity in the average case: the worst case cost of `n` consecutive appends is `O(n)`.
* Working with the pointers: the `&` and `*` operators.
* The `pop` function: with the `append` guarantees that the size of the additional memory used by the structure is a constant factor of the number of items in the list.
* The `realloc` function

```c
#include<stdio.h>
#include<stdlib.h>

/*
 * Dynamic array or list
 * 
 * */

struct list {
	int *p; /*array of integers */
	int n; /* number of items in the list*/
	int c;
};
typedef struct list list;


list zeros(int);
void show(list);
list append(list, int);
list pop(list, int*);

int main(){
	list a = zeros(0); /*the same of struct list */
	int i, e;
	
	for(i = 0; i < 40; i++){
		a = append(a, i);
		//show(a);
	}

	while( a.n > 0){
		a = pop(a, &e);
		/*printf("%d\n", e);
		show(a);*/
	}
	
}

list zeros(int n){
	list x;
	
	x.n = n;
	x.c = 2*n;
	
	if (n <= 0 ) 
		x.p = NULL;
	else
		x.p = malloc(n*sizeof(int));
	
	for(int i = 0; i < x.n; i++){
		x.p[i] = 0;
	}
	
	return x;
} 

void show(list x){
	int i;
	
	printf("[");
	for(i=0; i < x.n; i++){
		printf("%d ", x.p[i]); 
	}
	printf("]\n");
	printf("c = %d, n = %d\n", x.c, x.n);
}

list append_old(list x, int e){
	int i, *q;
	
	if (x.n == x.c){
		int new_c = 2*x.c+1; 
		q = malloc(new_c*sizeof(int));
		for( i = 0; i < x.n; i++){
			q[i] = x.p[i];
		}
		free(x.p);
		x.p = q;
		x.c = new_c;
	}
	x.p[x.n] = e;
	x.n += 1;
	
	return x;
}

list append(list x, int e){
	int i ,*q;
	
	if (x.n == x.c){
		int new_c = 2*x.c+1; 
		q = realloc(x.p, new_c*sizeof(int));
		x.p = q;
		x.c = new_c;
	}
	x.p[x.n] = e;
	x.n += 1;
	
	return x;
}


/*
 * Returns the last item of the list that is also removed from
 * the list.
 * 
 * We assume that x.n > 0
 * 
 * */
list pop(list x, int *q){
	int r = x.p[x.n-1];
	*q = r;
	x.n--;
	if (x.n < x.c/4){ /* integer division */
		x.p = realloc(x.p, (x.c/2+1)*sizeof(int));
		x.c = x.c/2+1;
	}
	return x;
}

```

* The `chr` type; the strings as arrays of characters; the `\0` symbol.

```c
#include <stdio.h>

int main(){
	char c = 'd';
	char s[] = "this is a C string";
	int len;
	
	printf("%c\n", c);
	printf("%s\n", s);
	
	s[5] = '\0';
	
	printf("%d\n", sizeof(s)/sizeof(char));
	
	printf("%s\n", s);
	
	len = 0;
	while( s[len] != '\0')
		len++;
	printf("%d\n", len);
}
```

