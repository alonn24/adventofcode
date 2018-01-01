package adventofcode2017

import scala.io.Source

object Day12 {
  lazy val input: String = Source.fromFile(s"2017/input/day-12.input").mkString.trim

  def main(args: Array[String]): Unit = {
    val graph = input.lines.foldLeft(Map[Int, List[Int]]()) {
      (res, row) => 
        row.split(" <-> ").toList match {
          case (a, b, :_) => println(s"$a $b")
        }
      res
    }
  }
}