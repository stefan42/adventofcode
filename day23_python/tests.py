import unittest
from puzzle import Machine, InstructionType

class TestMachineMethods(unittest.TestCase):

    def test_hlf_1(self):
        m = Machine([(InstructionType.hlf, 'a', None)])
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)

    def test_hlf_2(self):
        m = Machine([(InstructionType.hlf, 'a', None)])
        m.reg_a = 1
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)

    def test_hlf_3(self):
        m = Machine([(InstructionType.hlf, 'a', None)])
        m.reg_a = 4
        m.next_step()
        self.assertEqual(m.reg_a, 2)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)

    def test_hlf_4(self):
        m = Machine([(InstructionType.hlf, 'b', None)])
        m.reg_b = 16
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 8)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)



    def test_tpl_1(self):
        m = Machine([(InstructionType.tpl, 'a', None)])
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)

    def test_tpl_2(self):
        m = Machine([(InstructionType.tpl, 'a', None)])
        m.reg_a = 1
        m.next_step()
        self.assertEqual(m.reg_a, 3)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)

    def test_tpl_3(self):
        m = Machine([(InstructionType.tpl, 'b', None)])
        m.reg_b = 4
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 12)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)



    def test_inc_1(self):
        m = Machine([(InstructionType.inc, 'a', None)])
        m.next_step()
        self.assertEqual(m.reg_a, 1)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)


    def test_inc_2(self):
        m = Machine([(InstructionType.inc, 'a', None), (InstructionType.inc, 'a', None), (InstructionType.inc, 'a', None)])
        m.next_step()
        m.next_step()
        m.next_step()
        self.assertEqual(m.reg_a, 3)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 3)
        self.assertEqual(m.is_finished(), True)


    def test_jmp_1(self):
        m = Machine([(InstructionType.jmp, None, 42)])
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 42)
        self.assertEqual(m.is_finished(), True)

    def test_jmp_2(self):
        m = Machine([(InstructionType.jmp, None, -23)])
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, -23)
        self.assertEqual(m.is_finished(), True)


    def test_jie_1(self):
        m = Machine([(InstructionType.jie, 'a', 42)])
        m.reg_a = 6
        m.next_step()
        self.assertEqual(m.reg_a, 6)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 42)
        self.assertEqual(m.is_finished(), True)

    def test_jie_2(self):
        m = Machine([(InstructionType.jie, 'a', -23)])
        m.reg_a = 3
        m.next_step()
        self.assertEqual(m.reg_a, 3)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)


    def test_jio_1(self):
        m = Machine([(InstructionType.jio, 'a', 42)])
        m.reg_a = 1
        m.next_step()
        self.assertEqual(m.reg_a, 1)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 42)
        self.assertEqual(m.is_finished(), True)

    def test_jio_2(self):
        m = Machine([(InstructionType.jio, 'a', -23)])
        m.reg_a = 0
        m.next_step()
        self.assertEqual(m.reg_a, 0)
        self.assertEqual(m.reg_b, 0)
        self.assertEqual(m.inst_ptr, 1)
        self.assertEqual(m.is_finished(), True)


if __name__ == '__main__':
    unittest.main()
