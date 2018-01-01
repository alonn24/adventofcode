package adventofcode2017

import scala.io.Source

object Day12 {
  lazy val input: String = Source.fromFile(s"2017/input/day-12.input").mkString.trim

  def findGroup(graph: Map[String, List[String]], vil: String, found: Map[String, Boolean] = Map()): Map[String, Boolean] = {
    graph(vil).foldLeft(found + (vil -> true)) {
      (nFound, neighbor) =>
        if (nFound.contains(neighbor)) nFound 
        else findGroup(graph, neighbor, nFound + (vil -> true))
    }
  }

  def main(args: Array[String]): Unit = {
    val graph = input.lines.foldLeft(Map[String, List[String]]()) {
      (res, row) => 
        val num::connected::_ = row.split(" <-> ").toList
        val negh = connected.replaceAll("\\s", "").split(",").toList
        res + (num -> negh)
    }
    val g = findGroup(graph, "0")
    println(s"part1 ${g.keys.size}")

    val (count, _) = graph.keys.foldLeft((0, Map[String, Boolean]())) {
      case ((count, visited), cur) =>
        if (visited.contains(cur)) (count, visited)
        else (count + 1, findGroup(graph, cur, visited))
    }
    println(s"part2 $count")
  }
}