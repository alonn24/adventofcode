package adventofcode2017

object Day14 {
  lazy val input = "uugsqrei"
  type Region = (Int, Int)
  val sides = Set((0, 1), (1, 0), (-1, 0), (0, -1))

  def byteToBits(byte: Int, acc: List[Boolean] = List()): List[Boolean] = {
    if (acc.size == 4) acc
    else byteToBits(byte >>> 1, ((byte & 1) == 1) :: acc)
  }

  def visitGroup(region: Region, all: Set[Region], visited: Set[Region]): Set[Region] = {
    val neighbors = for { 
        side <- sides
        neighbor = (region._1 + side._1, region._2 + side._2)
        if (all.contains(neighbor) && !visited.contains(neighbor))
      } yield neighbor
    val newVisited = visited ++ neighbors
    neighbors.foldLeft(newVisited) { (visited, neighbor) => visitGroup(neighbor, all, visited) }
  }

  def main(args: Array[String]): Unit = {
    val rows = (0 until 128)
      .map(i => Day10.knotHash(s"$input-$i")
      .flatMap(c => byteToBits(Integer.parseInt(c.toString(), 16))))
    
    val bitCount = rows.foldLeft(0) { (count, row) => count + row.filter(_==true).length }
    println(s"part1 $bitCount")

    val all = (for(x <- 0 until 128; y <- 0 until 128; if rows(x)(y)) yield (x, y)).toSet
    val (groups, _) = all.foldLeft((0, Set[(Region)]())) {
      case ((count, visited), region) => 
        if (visited.contains(region)) (count, visited)
        else (count + 1, visitGroup(region, all, visited + region))
    }
    println(s"part2 $groups")
  }
}