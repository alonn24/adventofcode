package adventofcode2017

import scala.io.Source

object Day8 {
  private val inputRowRegex = """([a-z]+) ([a-z]+) (-?[0-9]+) if ([a-z]+) (.+) (-?[0-9]+)""".r
  lazy val input: String = Source.fromFile(s"2017/input/day-8.input").mkString.trim
  val equalities = Map[String, (Int, Int) => Boolean](
    ">" -> (_>_),
    "<" -> (_<_),
    ">=" -> (_>=_),
    "<=" -> (_<=_),
    "==" -> (_==_),
    "!=" -> (_!=_)
  )
  val oprs = Map[String, (Int, Int) => Int](
    "inc" -> (_+_),
    "dec" -> (_-_)
  )
  def main(args: Array[String]): Unit = {
    val (map, max) = input.lines.foldLeft((Map[String, Int](), 0)) {
      case ((map, max), inputRowRegex(reg, opr, amount, test, op, value)) => 
        if (equalities(op)(map.getOrElse(test, 0), value.toInt)) {
          val newVal = oprs(opr)(map.getOrElse(reg, 0), amount.toInt)
          (map + (reg -> newVal), Math.max(max, newVal))
        } else {
          (map, max)
        }
    }
    println(map.values.max)
    println(max)
  }
}
