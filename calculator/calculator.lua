print("Input first number.")
num1 = tonumber(io.read())
print("Input second number.")
num2 = tonumber(io.read())
print("Input calculation method.")
method = io.read()
if method == "+" then
  awnser = num1 + num2
end
if method == "-" then
  awnser = num1 - num2
end
if method == "*" then
  awnser = num1 * num2
end
if method == "/" then
  awnser = num1 / num2
end
print(awnser)