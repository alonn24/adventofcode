package adventofcode2017

import scala.io.Source

object Day9 {
  lazy val input: String = Source.fromFile(s"2017/input/day-9.input").mkString.trim

  def main(args: Array[String]): Unit = {
    val (part1, part2, count, ignor, garbage) = input.foldLeft((0, 0, 0, false, false)) {
      case ((part1, part2, count, true, garbage), value) => 
        (part1, part2, count, false, garbage)
      case ((part1, part2, count, false, true), value) => 
        val newIgnor = value == '!'
        val newGarbage = !(value == '>')
        val newPart2 = if (!newIgnor && newGarbage) part2+1 else part2
        (part1, newPart2, count, newIgnor, newGarbage)
      case ((part1, part2, count, false, false), '{') =>
        (part1, part2, count+1, false, false)
      case ((part1, part2, count, false, false), '}') =>
        (part1+count, part2, count-1, false, false)
      case ((part1, part2, count, false, false), '<') =>
        (part1, part2, count, false, true)
      case ((part1, part2, count, false, false), '!') =>
        (part1, part2, count+1, true, false)
      case (x, value) => x
    }
    println(part1);
    println(part2);
  }
}