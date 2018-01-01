package adventofcode2017

import scala.io.Source

object Day11 {
  lazy val input: String = Source.fromFile(s"2017/input/day-11.input").mkString.trim

  val map = Map[String, ((Int, Int, Int, Int)) => ((Int, Int, Int, Int))](
    "n" -> { case ((n, s, e, w)) => ((n+2, s-2, e, w)) },
    "ne" -> { case ((n, s, e, w)) => ((n+1, s-1, e+1, w-1)) },
    "se" -> { case ((n, s, e, w)) => ((n-1, s+1, e+1, w-1)) },
    "s" -> { case ((n, s, e, w)) => ((n-2, s+2, e, w)) },
    "sw" -> { case ((n, s, e, w)) => ((n-1, s+1, e-1, w+1)) },
    "nw" -> { case ((n, s, e, w)) => ((n+1, s-1, e-1, w+1)) }
  )

  def getDistance(pos:(Int, Int, Int, Int)): Int = {
    pos match {
      case (n, s, e, w) => 
        val absn = Math.abs(n)
        val absw = Math.abs(w)
        absw + (absn - absw) / 2
    }
  }

  def main(args: Array[String]): Unit = {
    val steps = input.split(",").toList
    val (pos, max) = steps.foldLeft(((0, 0, 0, 0), 0)) {
      case (((n, s, e, w), max), step) => 
        val pos = map(step)((n, s, e, w))
        (pos, Math.max(max, getDistance(pos)))
    }

    println(s"part1 ${getDistance(pos)}")
    println(s"part2 $max")
  }
}