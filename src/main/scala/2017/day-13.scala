package adventofcode2017

import scala.io.Source

object Day13 {

  def isCoughtOnLayer(layer: Option[Int], step: Int): Boolean = {
    layer match {
      case None => false
      case Some(depth) => 
        val devider = depth*2 - 2
        step % devider == 0
    }
  }

  def willGetCought(layers: Int, map: Map[Int, Int], delay: Int): Boolean = {
    (0 until layers+1).foldLeft(false) {
      (cought, step) => cought || 
        isCoughtOnLayer(map.get(step), step+delay)
    }
  }

  def findDelay(layers: Int, map: Map[Int, Int], delay: Int = 0): Int = {
    if (!willGetCought(layers, map, delay)) delay
    else findDelay(layers, map, delay+1)
  }

  lazy val input: String = Source.fromFile(s"2017/input/day-13.input").mkString.trim
   def main(args: Array[String]): Unit = {
    val map = input.lines.foldLeft(Map[Int, Int]()) {
      (map, row) => 
        val layer::depth::_ = row.split(": ").toList
        map + (layer.toInt -> depth.toInt)
    }
    val layers = map.keys.foldLeft(0) { Math.max(_, _) }

    val sev = (0 until layers+1).foldLeft(0) {
      (sev, step) => 
        if (isCoughtOnLayer(map.get(step), step)) 
          sev + (map.getOrElse(step, 0) * step)
        else
          sev
    }
    println(s"part1 $sev")

    val delay = findDelay(layers, map)
    println(s"part2 $delay")
   }
}