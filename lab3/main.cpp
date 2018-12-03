#include <iostream>
#include <math.h>

using namespace std;

 unsigned long long int factorial(unsigned long long int a)
{
    if(a == 1) return a;
    else if(a == 0) return 1;

    return a * factorial(a - 1);
}

unsigned long long int combinationC(unsigned long long int numinator,unsigned long long int denominator)
{
    return factorial(denominator) / (factorial(numinator) * factorial(denominator - numinator));
}

void change(unsigned long long int *m,unsigned long long int l,unsigned long long int n )
{
  if( l == n - 1 )
  {
    for( unsigned long long int i=0; i < n; i++) cout << m[i];
    cout << ' ';
  }
  else
  {
    for(unsigned long long int i=l; i < n; i++ )
    {
      int tmp = m[l];
      m[l] = m[i];
      m[i] = tmp;
      change( m, l+1, n );
      tmp = m[l];
      m[l] = m[i];
      m[i] = tmp;
    }
  }
}

int main()
{

 unsigned long long int n;
  cout << "Input N, please:\n";
  cin >> n;
  unsigned long long int *m = new unsigned long long int[n];

  for( int i = 0; i<n; i++)
    m[i] = i + 1;

  change( m, 0, n );
  cout << endl;

  int x, y ,p;
    cout << "\nInput x:";
    cin >> x;
    cout << "Input y:";
    cin >> y;
    cout << "imput power (z)";
    cin >> p;


   unsigned long long int binom = 0;

    for(unsigned long long int i = 0; i <= p; ++i)
    {
        binom += combinationC(i, p) * pow(x, i) * pow(y, p - i);
    }

    cout <<"Binom for (x+y)^z = \n";

    for(unsigned long long int i = 0; i <= p; ++i)
    {
        cout <<"(x^" << i <<") * (y^" <<p - i <<") * " << combinationC(i, p);
        if(i != p) cout <<"  +  ";
    }

    cout <<" = \n" <<binom <<"\n";

        return 0;


}
