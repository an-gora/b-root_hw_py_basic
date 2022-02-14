from enum import Enum, unique
from typing import Optional, TypeAlias, Iterable


T_CITY_NAME: TypeAlias = 'City'
T_EDGE_WEIGHT: TypeAlias = float


@unique
class City(Enum):
    kyiv = 'Kyiv'
    kukuevo = 'Kukuevo'
    lviv = 'Lviv'
    poznan = 'Poznan'
    uman = 'Uman'
    odessa = 'Odessa'

    def __str__(self):
        return self.value

    __repr__ = __str__


class Vertex:

    def __init__(self, key: T_CITY_NAME) -> None:
        self._id = key
        self.connected_to: dict["Vertex", T_EDGE_WEIGHT] = {}

    def add_neighbor(self, neighbor, weight: T_EDGE_WEIGHT = 0) -> None:
        self.connected_to[neighbor] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self) -> tuple["Vertex", ...]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> T_CITY_NAME:
        return self._id


class Graph:

    def __init__(self) -> None:
        self.vertices_dict: dict[T_CITY_NAME, Vertex] = {}
        self.num_vertices: int = 0

    def add_vertex(self, key: T_CITY_NAME):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: T_CITY_NAME) -> Optional[Vertex]:
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def __contains__(self, n: T_CITY_NAME) -> bool:
        return n in self.vertices_dict

    def add_edge(self, city_from: T_CITY_NAME, city_to: T_CITY_NAME, weight: T_EDGE_WEIGHT = 0) -> None:
        if city_from not in self.vertices_dict:
            self.add_vertex(city_from)
        if city_to not in self.vertices_dict:
            self.add_vertex(city_to)
        self.vertices_dict[city_from].add_neighbor(self.vertices_dict[city_to], weight)

    def get_vertices(self) -> tuple[T_CITY_NAME, ...]:
        return tuple(self.vertices_dict.keys())

    def __iter__(self) -> Iterable[Vertex]:
        return iter(self.vertices_dict.values())


def main():
    my_graph = Graph()

    for city in City:
        my_graph.add_vertex(city)

    my_graph.add_edge(City.kyiv, City.kukuevo, 5)
    my_graph.add_edge(City.lviv, City.odessa, 2)
    my_graph.add_edge(City.lviv, City.poznan, 24)
    my_graph.add_edge(City.poznan, City.uman, 22)
    my_graph.add_edge(City.kyiv, City.odessa, 222)

    for city in my_graph:
        for city_neighbor in city.get_connections():
            print(f'( {city.get_id()} , {city_neighbor.get_id()} )')
    # print(my_graph.get_vertex(City.kyiv))
    # print(g.get_vertex(2))


if __name__ == "__main__":
    main()