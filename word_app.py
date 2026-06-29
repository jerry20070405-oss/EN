import streamlit as st
import random

# 1. 整合 Unit 7 & Unit 8 所有核心單字、詞性、中文意思與英文定義
WORD_BANK = {
    "Unit 7: Energy Solutions": {
        "capacity": {"pos": "n.", "zh": "能力；生產力；容量", "def": "ability to do something"},
        "decline": {"pos": "v.", "zh": "減少；衰退；下降", "def": "to gradually become less"},
        "disposal": {"pos": "n.", "zh": "清除；處理；丟棄", "def": "the act or means of getting rid of something"},
        "eliminate": {"pos": "v.", "zh": "消除；移除；淘汰", "def": "to remove (something that is not wanted or needed) ; to get rid of (something)"},
        "equivalent": {"pos": "adj.", "zh": "等值的；相等的", "def": "having the same amount, value, purpose, qualities, etc."},
        "guarantee": {"pos": "v.", "zh": "保證；承諾", "def": "to promise that something will be done or will happen"},
        "protest": {"pos": "v.", "zh": "抗議；反對", "def": "a formal and solemn declaration of objection"},
        "steep": {"pos": "adj.", "zh": "急遽的；陡峭的", "def": "going very quickly from low to high or from high to low"},
        "substitute": {"pos": "n.", "zh": "替代品；代替者", "def": "a thing or person that is used instead of another thing or person"},
        "utilize": {"pos": "v.", "zh": "利用；使用", "def": "to use something in an effective way"},
        "comprehensive": {"pos": "adj.", "zh": "全面的；廣泛的；包含所有的", "def": "including all or everything"},
        "cooling": {"pos": "adj.", "zh": "冷卻的；降溫的", "def": "the process of becoming cooler"},
        "distribute": {"pos": "v.", "zh": "分發；分配；分銷", "def": "to share things among a group of people"},
        "efficiency": {"pos": "n.", "zh": "效率；效能", "def": "the quality of doing something well and effectively, without wasting time, money, or energy"},
        "emissions": {"pos": "n.", "zh": "排放物；散發", "def": "the act of sending out light, heat, gas etc."},
        "regulation": {"pos": "n.", "zh": "規定；法規；條例", "def": "an official rule or order"},
        "resident": {"pos": "n.", "zh": "居民；住戶", "def": "someone who lives or stays in a particular place"},
        "sustainable": {"pos": "adj.", "zh": "永續的；可持續的", "def": "able to continue without causing damage to the environment"},
        "unrealistic": {"pos": "adj.", "zh": "不切實際的；不合理的", "def": "not reasonable or sensible"},
        "wealthy": {"pos": "adj.", "zh": "富裕的；有錢的", "def": "having a lot of money, possessions etc."}
    },
    "Unit 8: Epic Engineering": {
        "acquire": {"pos": "v.", "zh": "取得；獲得；學到", "def": "to get (something)"},
        "citizen": {"pos": "n.", "zh": "公民；國民", "def": "a person who legally belongs to a country and has the rights and protection of that country"},
        "demolish": {"pos": "v.", "zh": "拆除；摧毀（建築物等）", "def": "to destroy (a building, bridge, etc.)"},
        "former": {"pos": "adj.", "zh": "前任的；昔日的；先前的", "def": "used to say what someone or something was in the past"},
        "monument": {"pos": "n.", "zh": "紀念碑；歷史遺跡", "def": "a building, statue, or other large structure that is built to remind people of an important event"},
        "proposal": {"pos": "n.", "zh": "提案；建議；計劃", "def": "a plan or suggestion which is made formally to an official person or group"},
        "regional": {"pos": "adj.", "zh": "地區的；區域性的", "def": "a part of a country, of the world, etc., that is different or separate from other parts in some way"},
        "renovation": {"pos": "n.", "zh": "整修；翻新；裝修", "def": "When you make changes and repairs to (an old house, building, room, etc.) so that it is back in good condition"},
        "repair": {"pos": "v.", "zh": "修理；修補", "def": "to put (something that is broken or damaged) back into good condition"},
        "transport": {"pos": "v.", "zh": "運輸；運送", "def": "to take goods or people from one place to another"},
        "accessible": {"pos": "adj.", "zh": "可到達的；易接近的；可使用的", "def": "capable of being reached"},
        "border": {"pos": "n.", "zh": "邊界；國境；邊緣", "def": "a line that indicates a boundary"},
        "dense": {"pos": "adj.", "zh": "稠密的；濃厚的；密集的", "def": "thick; difficult to go or see through"},
        "enormous": {"pos": "adj.", "zh": "巨大的；龐大的", "def": "extremely large"},
        "illustrate": {"pos": "v.", "zh": "說明；闡明；（用實例）說明", "def": "to show the meaning or truth of something more clearly, usually by giving examples"},
        "impact": {"pos": "n.", "zh": "巨大影響；衝擊；效果", "def": "a powerful or major influence or effect"},
        "occur": {"pos": "v.", "zh": "發生", "def": "to happen"},
        "partially": {"pos": "adv.", "zh": "部分地；不完全地", "def": "somewhat but not completely ; to some extent or in some degree"},
        "practical": {"pos": "adj.", "zh": "實際的；實用的；切合實際的", "def": "relating to what is real rather than to what is possible or imagined"},
        "ruin": {"pos": "n.", "zh": "毀滅；廢墟；破產", "def": "a state of complete destruction ; a state of being ruined"}
    }
}

st.set_page_config(page_title="Unit 7 & 8 中翻英單字練習", page_icon="✍️", layout="centered")

st.title("✍️ Unit 7 & 8 中翻英單字練習")
st.write("看中文輸入正確的英文單字，點擊側邊欄可以切換模式與單元！")

# 側邊欄設定
st.sidebar.header("⚙️ 設定練習範圍")
unit_choice = st.sidebar.selectbox("選擇單元", ["全部單元", "Unit 7: Energy Solutions", "Unit 8: Epic Engineering"])
mode_choice = st.sidebar.radio("練習模式", ["看中文拼英文 (填空題)", "看中文選英文 (多選題)"])

# 建立當前單字庫
current_words = {}
if unit_choice == "全部單元":
    current_words.update(WORD_BANK["Unit 7: Energy Solutions"])
    current_words.update(WORD_BANK["Unit 8: Epic Engineering"])
else:
    current_words.update(WORD_BANK[unit_choice])

word_list = list(current_words.keys())

# 初始化 Session State 變數 (修正：加入 is_correct 與 wrong_ans 的初始化)
if "current_question_word" not in st.session_state or st.session_state.get("prev_unit") != unit_choice:
    st.session_state.current_question_word = random.choice(word_list)
    st.session_state.prev_unit = unit_choice
    st.session_state.answered = False
    st.session_state.is_correct = False
    st.session_state.wrong_ans = ""
    st.session_state.user_score = 0
    st.session_state.total_questions = 0
    st.session_state.options = []

q_word = st.session_state.current_question_word
q_info = current_words[q_word]

# 重新出題函數
def next_question():
    st.session_state.current_question_word = random.choice(word_list)
    st.session_state.answered = False
    st.session_state.is_correct = False
    st.session_state.wrong_ans = ""
    st.session_state.options = []

# --- 模式一：看中文拼英文 ---
if mode_choice == "看中文拼英文 (填空題)":
    st.subheader("請根據中文提示，輸入正確的英文單字：")
    st.info(f"**中文意思 ({q_info['pos']})**：{q_info['zh']}")
    st.caption(f"📖 英文課本定義：*{q_info['def']}*")
    
    # 提示字首字尾與長度
    hint = f"💡 提示：字首為 '{q_word[0]}', 字尾為 '{q_word[-1]}', 總共 {len(q_word)} 個字母"
    st.caption(hint)
    
    # 文字輸入框（使用 form 包裹，按 Enter 即可直接提交）
    with st.form(key="input_form", clear_on_submit=True):
        user_input = st.text_input("請輸入英文單字：").strip().lower()
        submit_btn = st.form_submit_button("提交答案")
        
        if submit_btn:
            if not st.session_state.answered:
                st.session_state.answered = True
                st.session_state.total_questions += 1
                if user_input == q_word.lower():
                    st.session_state.is_correct = True
                    st.session_state.user_score += 1
                else:
                    st.session_state.is_correct = False
                    st.session_state.wrong_ans = user_input

    # 在 Form 外面顯示結果
    if st.session_state.answered:
        if st.session_state.is_correct:
            st.success(f"🎉 太厲害了！完全正確：**{q_word}**")
        else:
            st.error(f"❌ 拼錯囉！你輸入的是 '{st.session_state.wrong_ans}'，正確答案是：**{q_word}**")

# --- 模式二：看中文選英文 ---
else:
    st.subheader("請選出最符合該中文意思的英文單字：")
    st.info(f"**中文意思 ({q_info['pos']})**：{q_info['zh']}")
    st.caption(f"📖 英文課本定義：*{q_info['def']}*")
    
    # 產生多選題選項
    if not st.session_state.options:
        correct_word = q_word
        wrong_words = [w for w in word_list if w != q_word]
        sampled_wrong = random.sample(wrong_words, min(3, len(wrong_words)))
        options = sampled_wrong + [correct_word]
        random.shuffle(options)
        st.session_state.options = options

    # 顯示選項按鈕
    for idx, opt in enumerate(st.session_state.options):
        if st.button(f"✨ {opt}", key=f"btn_{opt}", use_container_width=True):
            if not st.session_state.answered:
                st.session_state.answered = True
                st.session_state.total_questions += 1
                if opt == q_word:
                    st.success("🎉 答對了！概念很清晰喔！")
                    st.session_state.user_score += 1
                else:
                    st.error(f"❌ 答錯囉！正確答案是：**{q_word}**")

# --- 共用控制與計分板 ---
st.divider()
col1, col2 = st.columns([3, 1])

with col1:
    if st.session_state.answered:
        st.button("下一題 ➡️", on_click=next_question, type="primary")
    else:
        st.button("跳過此題 ⏭️", on_click=next_question)

with col2:
    st.metric("目前得分", f"{st.session_state.user_score} / {st.session_state.total_questions}")

# 單字列表對照表
with st.expander("📚 查看當前範圍的所有單字一覽表"):
    for w in sorted(word_list):
        st.write(f"**{w}** ({current_words[w]['pos']}) 👉 {current_words[w]['zh']}")