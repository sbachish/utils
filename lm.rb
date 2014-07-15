class LinearRegression

  def initialize(x, y)
    @x, @y = x, y
    if @x.length != @y.length
      raise "x & y need to be same length"
    end
  end

  def mean(values)
    total = values.reduce(0) { |sum, x| x + sum }
    Float(total) / Float(values.length)
  end


  def intercept
    mean(@y) - (slope * mean(@x))
  end


  def slope
    x_mean = mean(@x)
    y_mean = mean(@y)

    numerator = (0...@x.length).reduce(0) do |sum, i|
      sum + ((@x[i] - x_mean) * (@y[i] - y_mean))
    end

    denominator = @x.reduce(0) do |sum, x|
      sum + ((x - x_mean) ** 2)
    end

    (numerator / denominator)
  end

end
