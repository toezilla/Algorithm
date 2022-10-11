def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        idx = 0
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                if skill.find(skill_tree[i]) == idx:
                    idx += 1
                    continue
                break

        else:
            answer += 1

    return answer