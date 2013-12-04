def find_deviation(v, d)
    # Write your code here
    # To print results to the standard output you can use puts
    # Example puts "Hello world!"
    result = []
    finish = d
    while finish <= v.length do
        result << v[finish-d...finish].max - v[finish-d...finish].min
        finish += 1
    end
    p result.max
end
