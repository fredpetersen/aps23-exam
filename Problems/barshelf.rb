class FenwickTree
  def initialize(n)
    @tree = Array.new(n + 1, 0)
    @max = n
  end

  def update(index, value)
    while index <= @max
      @tree[index] += value
      index += index & (-index)
    end
  end

  def sum(right)
    res = 0

    while right > 0
      res += @tree[right]
      right -= right & (-right)
    end

    res
  end
end

def get_inversion_count(trees, array, indices, max)
  array.reverse_each do |element|
    index = indices[element]
    half = indices[element / 2]

    trees[0].update(index, 1)
    trees[1].update(index, trees[0].sum(half))
    trees[2].update(index, trees[1].sum(half))
  end

  trees[2].sum(max)
end

_n = gets.to_i
for_indexing = []
array = []
indices = {}
counter = 0

gets.split.each do |i|
  x = i.to_i
  for_indexing << x
  for_indexing << x * 2
  array << x * 2
end

for_indexing.sort.each do |i|
  next if indices.key?(i)

  indices[i] = counter += 1
end

trees = []
3.times { trees.append(FenwickTree.new(counter)) }

puts get_inversion_count(trees, array, indices, counter)
