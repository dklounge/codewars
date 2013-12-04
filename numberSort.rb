# sort numbers in an array

def solution(nums)
  answer = []
  if nums == nil
    return answer
  else
    counter = nums.length - 1
    while counter >= 0
      answer << nums.min
      nums.delete(nums.min)
      counter -= 1
    end
  end
  return answer
end

p solution([1, 2, 10, 50, 5])
