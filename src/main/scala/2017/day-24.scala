package adventofcode2017

import scala.io.Source

object Day24 {
  def getBridges(prev: List[(Int, Int)], ports:List[(Int, Int)]): List[List[(Int, Int)]] = {
    val (_,b) = prev.last
    val candidates = ports.filter({ case (c, d) => c == b || d == b})
    candidates match {
      case Nil => List(prev)
      case _ => {
        candidates.flatMap(port => {
          val nextPorts = ports.filter(x => x != port)
          val portToAdd = port match {
            case (c,d) => if (c == b) (c,d) else (d,c)
          }
          val nextPrev = prev :+ portToAdd
          getBridges(nextPrev, nextPorts)
        })
      }
    }
  }
  private val inputRowRegex = """(\d+)/(\d+)""".r
  lazy val input: String = Source.fromFile(s"2017/input/day-24.input").mkString.trim

  def sum(bridge: List[(Int, Int)]): Int = bridge.foldLeft(0)((res, port) => res + port._1 + port._2)

  def main(args: Array[String]): Unit = {
    val ports = input.lines.map(str => str match {
      case inputRowRegex(a, b) => (a.toInt, b.toInt)
    }).toList
    val bridges = getBridges(List((0,0)), ports)
    val winner = bridges.reduceLeft((a,b) => if(a.size>b.size || a.size == b.size && sum(a) > sum(b)) a else b)
    println(sum(winner))
  }
}
