module SortUnitFlatRTL__nbits_8 (
	clk,
	in_,
	in_val,
	out,
	out_val,
	reset
);
	reg _sv2v_0;
	input wire [0:0] clk;
	input wire [31:0] in_;
	input wire [0:0] in_val;
	output reg [31:0] out;
	output reg [0:0] out_val;
	input wire [0:0] reset;
	reg [7:0] elm_S1 [0:3];
	reg [7:0] elm_S2 [0:3];
	reg [7:0] elm_S3 [0:3];
	reg [7:0] elm_next_S1 [0:3];
	reg [7:0] elm_next_S2 [0:3];
	reg [7:0] elm_next_S3 [0:3];
	reg [0:0] val_S1;
	reg [0:0] val_S2;
	reg [0:0] val_S3;
	always @(*) begin : stage_S1
		if (_sv2v_0)
			;
		if (elm_S1[2'd0] <= elm_S1[2'd1]) begin
			elm_next_S1[2'd0] = elm_S1[2'd0];
			elm_next_S1[2'd1] = elm_S1[2'd1];
		end
		else begin
			elm_next_S1[2'd0] = elm_S1[2'd1];
			elm_next_S1[2'd1] = elm_S1[2'd0];
		end
		if (elm_S1[2'd2] <= elm_S1[2'd3]) begin
			elm_next_S1[2'd2] = elm_S1[2'd2];
			elm_next_S1[2'd3] = elm_S1[2'd3];
		end
		else begin
			elm_next_S1[2'd2] = elm_S1[2'd3];
			elm_next_S1[2'd3] = elm_S1[2'd2];
		end
	end
	always @(*) begin : stage_S2
		if (_sv2v_0)
			;
		if (elm_S2[2'd0] <= elm_S2[2'd2]) begin
			elm_next_S2[2'd0] = elm_S2[2'd0];
			elm_next_S2[2'd2] = elm_S2[2'd2];
		end
		else begin
			elm_next_S2[2'd0] = elm_S2[2'd2];
			elm_next_S2[2'd2] = elm_S2[2'd0];
		end
		if (elm_S2[2'd1] <= elm_S2[2'd3]) begin
			elm_next_S2[2'd1] = elm_S2[2'd1];
			elm_next_S2[2'd3] = elm_S2[2'd3];
		end
		else begin
			elm_next_S2[2'd1] = elm_S2[2'd3];
			elm_next_S2[2'd3] = elm_S2[2'd1];
		end
	end
	always @(*) begin : stage_S3
		if (_sv2v_0)
			;
		if (elm_S3[2'd1] <= elm_S3[2'd2]) begin
			elm_next_S3[2'd1] = elm_S3[2'd1];
			elm_next_S3[2'd2] = elm_S3[2'd2];
		end
		else begin
			elm_next_S3[2'd1] = elm_S3[2'd2];
			elm_next_S3[2'd2] = elm_S3[2'd1];
		end
		elm_next_S3[2'd0] = elm_S3[2'd0];
		elm_next_S3[2'd3] = elm_S3[2'd3];
	end
	function automatic [1:0] sv2v_cast_2;
		input reg [1:0] inp;
		sv2v_cast_2 = inp;
	endfunction
	always @(posedge clk) begin : pipereg_S0S1
		if (reset)
			val_S1 <= 1'd0;
		else
			val_S1 <= in_val;
		begin : sv2v_autoblock_1
			reg [31:0] i;
			for (i = 1'd0; i < 3'd4; i = i + 1'd1)
				elm_S1[sv2v_cast_2(i)] <= in_[(3 - sv2v_cast_2(i)) * 8+:8];
		end
	end
	always @(posedge clk) begin : pipereg_S1S2
		if (reset)
			val_S2 <= 1'd0;
		else
			val_S2 <= val_S1;
		begin : sv2v_autoblock_2
			reg [31:0] i;
			for (i = 1'd0; i < 3'd4; i = i + 1'd1)
				elm_S2[sv2v_cast_2(i)] <= elm_next_S1[sv2v_cast_2(i)];
		end
	end
	always @(posedge clk) begin : pipereg_S2S3
		if (reset)
			val_S3 <= 1'd0;
		else
			val_S3 <= val_S2;
		begin : sv2v_autoblock_3
			reg [31:0] i;
			for (i = 1'd0; i < 3'd4; i = i + 1'd1)
				elm_S3[sv2v_cast_2(i)] <= elm_next_S2[sv2v_cast_2(i)];
		end
	end
	always @(posedge clk) begin : pipereg_S3Out
		if (reset)
			out_val <= 1'd0;
		else
			out_val <= val_S3;
		begin : sv2v_autoblock_4
			reg [31:0] i;
			for (i = 1'd0; i < 3'd4; i = i + 1'd1)
				out[(3 - sv2v_cast_2(i)) * 8+:8] <= elm_next_S3[sv2v_cast_2(i)];
		end
	end
	initial _sv2v_0 = 0;
endmodule
