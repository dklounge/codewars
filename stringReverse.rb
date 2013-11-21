# reverse a string
def solution(str)
  counter = str.length - 1
  word = ""
  while counter >= 0
    word << str[counter]
    counter -= 1
  end
  return word
end

p solution("world")
