import { FernGeneratorExec } from "@fern-fern/generator-exec-client";
import { mkdir, writeFile } from "fs/promises";
import path from "path";

export async function writeGitHubWorkflows({
    config,
    githubOutputMode,
}: {
    config: FernGeneratorExec.GeneratorConfig;
    githubOutputMode: FernGeneratorExec.GithubOutputMode;
}): Promise<void> {
    if (githubOutputMode.publishInfo.type != "npm") {
        throw new Error(
            `Expected to receive npm publish info but received ${githubOutputMode.publishInfo.type} instead`
        );
    }
    const workflowYaml = `name: ci

    on: [push]
    
    jobs:
      compile:
        runs-on: ubuntu-latest
    
        steps:
          - uses: actions/checkout@v2
    
          - name: Set up node
            uses: actions/setup-node@v2
    
          - name: compile
            run: yarn && yarn build
      
      publish:
        needs: [ compile ]
        if: github.event_name == 'push' && contains(github.ref, 'refs/tags/')
        runs-on: ubuntu-latest
        
        steps:
          - uses: actions/checkout@v2
    
          - name: Set up node
            uses: actions/setup-node@v2
    
          - run: yarn install
    
          - name: Publish to NPM
            run: |
              npm config set //registry.npmjs.org/:_authToken \${NPM_TOKEN}
              npm publish --ignore-scripts
            env:
              NPM_TOKEN: \${secrets.${githubOutputMode.publishInfo.tokenEnvironmentVariable}}`;
    const githubWorkflowsDir = path.join(config.output.path, ".github", "workflows");
    await mkdir(githubWorkflowsDir, { recursive: true });
    await writeFile(`${githubWorkflowsDir}/ci.yml`, workflowYaml);
}
