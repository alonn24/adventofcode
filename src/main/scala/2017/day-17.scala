package adventofcode2017

object Day17 {
  val input = 316

  def main(args: Array[String]): Unit = {
    val (buffer, _) = (1 until 2018).foldLeft((Array[Int](0), 0)) {
      case ((buffer, pos), i) => 
        val newPos = ((pos + input) % buffer.length) + 1
        val newBuffer = buffer.slice(0, newPos) ++ Array(i) ++ buffer.slice(newPos, buffer.length)
        (newBuffer, newPos)
    }
    val index2017 = buffer.indexOf(2017)
    println(s"part1: ${buffer(index2017+1)}")

    val (res, _, _) = (1 until 50000000).foldLeft((0, 1, 0)) {
      case ((res, length, pos), i) =>
        val newPos = ((pos + input) % length) + 1
        val newRes = if (newPos == 1) i else res
        (newRes, length+1, newPos)
    }
    println(s"part2: ${res}")
  }
}