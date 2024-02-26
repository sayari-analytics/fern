/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.problem.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.trace.core.ObjectMappers;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = ProblemDescription.Builder.class)
public final class ProblemDescription {
    private final List<ProblemDescriptionBoard> boards;

    private final Map<String, Object> additionalProperties;

    private ProblemDescription(List<ProblemDescriptionBoard> boards, Map<String, Object> additionalProperties) {
        this.boards = boards;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("boards")
    public List<ProblemDescriptionBoard> getBoards() {
        return boards;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof ProblemDescription && equalTo((ProblemDescription) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(ProblemDescription other) {
        return boards.equals(other.boards);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.boards);
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static Builder builder() {
        return new Builder();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder {
        private List<ProblemDescriptionBoard> boards = new ArrayList<>();

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        public Builder from(ProblemDescription other) {
            boards(other.getBoards());
            return this;
        }

        @JsonSetter(value = "boards", nulls = Nulls.SKIP)
        public Builder boards(List<ProblemDescriptionBoard> boards) {
            this.boards.clear();
            this.boards.addAll(boards);
            return this;
        }

        public Builder addBoards(ProblemDescriptionBoard boards) {
            this.boards.add(boards);
            return this;
        }

        public Builder addAllBoards(List<ProblemDescriptionBoard> boards) {
            this.boards.addAll(boards);
            return this;
        }

        public ProblemDescription build() {
            return new ProblemDescription(boards, additionalProperties);
        }
    }
}