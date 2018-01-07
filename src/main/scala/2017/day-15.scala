package adventofcode2017

object Day15 {
  val inputA = 289L
  val inputB = 629L
  val factorA = 16807L
  val factorB = 48271L
  val mod = 2147483647

  def next(num: Long, factor: Long, crit: (Long) => Boolean = (num) => true): Long = {
    val value = (num * factor) % mod
    if (crit(value) == true) value else next(value, factor, crit)
  }

  def main(args: Array[String]): Unit = {
    val (_, _, count1) = (0 until 40000000).foldLeft(inputA, inputB, 0) {
      case ((a, b, count), _) => 
        val nextA = next(a, factorA)
        val nextB = next(b, factorB)
        val nextCount = if ((nextA & 0xffff) == (nextB & 0xffff)) count+1 else count
        (nextA, nextB, nextCount)
    }
    println(s"part1 $count1")

    val (_, _, count2) = (0 until 5000000).foldLeft(inputA, inputB, 0) {
      case ((a, b, count), _) => 
        val nextA = next(a, factorA, n => (n % 4) == 0)
        val nextB = next(b, factorB, n => (n % 8) == 0)
        val nextCount = if ((nextA & 0xffff) == (nextB & 0xffff)) count+1 else count
        (nextA, nextB, nextCount)
    }
    println(s"part2 $count2")
  }
}