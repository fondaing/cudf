# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

class List(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsList(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = List()
        x.Init(buf, n + offset)
        return x

    # List
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def ListStart(builder): builder.StartObject(0)
def ListEnd(builder): return builder.EndObject()