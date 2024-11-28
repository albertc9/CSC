module SortUnitFlatRTL__nbits_8
(
  input  logic        clk,          // 时钟信号
  input  logic        reset,        // 复位信号
  input  logic [3:0][7:0] in_,      // 输入：4 个 8 位宽数据
  input  logic        in_val,       // 输入有效信号
  output logic [3:0][7:0] out,      // 输出：4 个 8 位宽数据
  output logic        out_val       // 输出有效信号
);

  // 中间信号和寄存器定义
  logic [3:0][7:0] elm_S1;          // 中间寄存器，存储排序过程数据
  logic [3:0][7:0] elm_next_S1;     // 中间寄存器，存储下一阶段数据
  logic           val_S1;          // 中间有效信号

  // 排序逻辑块 (stage_S1)：比较输入数据对 (0,1) 和 (2,3)，并交换顺序
  always_comb begin : stage_S1
    // 比较 (0,1)
    if ( elm_S1[0] <= elm_S1[1] ) begin
      elm_next_S1[0] = elm_S1[0];
      elm_next_S1[1] = elm_S1[1];
    end else begin
      elm_next_S1[0] = elm_S1[1];
      elm_next_S1[1] = elm_S1[0];
    end

    // 比较 (2,3)
    if ( elm_S1[2] <= elm_S1[3] ) begin
      elm_next_S1[2] = elm_S1[2];
      elm_next_S1[3] = elm_S1[3];
    end else begin
      elm_next_S1[2] = elm_S1[3];
      elm_next_S1[3] = elm_S1[2];
    end
  end

  // 寄存器块 (pipereg_S0S1)：处理复位和输入信号传递到 S1 阶段
  always_ff @(posedge clk) begin : pipereg_S0S1
    if ( reset ) begin
      val_S1 <= 1'b0;               // 复位：无效信号
      elm_S1 <= 4'b0;               // 复位：清空寄存器
    end else begin
      val_S1 <= in_val;             // 输入有效信号传递
      elm_S1 <= in_;                // 输入数据存入寄存器
    end
  end

  // 输出逻辑：传递排序后的数据到输出
  assign out = elm_next_S1;         // 排序结果传递到输出
  assign out_val = val_S1;          // 有效信号传递到输出

endmodule