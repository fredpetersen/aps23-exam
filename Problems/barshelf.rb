class FenwickTree
  def initialize(n, max)
    @tree = Array.new(n, 0)
    @max = max
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

def get_inversion_count(trees, array, max)
  array.reverse_each do |index|
    trees[0].update(index, 1)
    trees[1].update(index, trees[0].sum(index / 2))
    trees[2].update(index, trees[1].sum(index / 2))
  end

  trees[2].sum(max)
end

n = gets.to_i
array = gets.split.map(&:to_i)
max = array.max

trees = []
3.times { trees.append(FenwickTree.new(max + 1, max))}

puts get_inversion_count(trees, array, max)
