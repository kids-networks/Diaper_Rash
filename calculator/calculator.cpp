#include <iostream>
using namespace std;

int main()  {
  cout << "Welcome to the Calculator Application.\n";
  double num1, num2, awnser;
  string method;
  cout << "Input calculation method.\n";
  cin >> method;
  cout << "Input the first number.\n";
  cin >> num1;
  cout << "Input the second number.\n";
  cin >> num2;
  if (method == "+")  {
    awnser = num1 + num2;
  }
  if (method == "-")  {
    awnser = num1 - num2;
  }
  if (method == "*")  {
    awnser = num1 * num2;
  }
  if (method == "/")  {
    awnser = num1 / num2;
  }
  cout << "The awnser is " + std::to_string(awnser) + ".";
  return 0;
}
